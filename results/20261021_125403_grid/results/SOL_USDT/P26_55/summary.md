# EMA Hourly Continuation — SOL/USDT P26_55

**Symbol:** SOL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.7389 |
| net_win_rate | 0.5120 |
| gross_profit_factor | 1.0484 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -1.8663 |
| sortino_ratio | -0.5203 |
| max_drawdown | 0.4743 |
| cagr | -0.2116 |
| net_avg_win | 66.2535 |
| net_avg_loss | -94.0742 |
| avg_hold_time_bars | 7.3387 |
| exposure | 0.1251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
