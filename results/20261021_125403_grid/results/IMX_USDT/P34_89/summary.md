# EMA Hourly Continuation — IMX/USDT P34_89

**Symbol:** IMX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.8557 |
| net_win_rate | 0.5227 |
| gross_profit_factor | 1.0804 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -0.9472 |
| sortino_ratio | -0.2929 |
| max_drawdown | 0.3152 |
| cagr | -0.1286 |
| net_avg_win | 71.8462 |
| net_avg_loss | -91.9439 |
| avg_hold_time_bars | 10.0886 |
| exposure | 0.2114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
