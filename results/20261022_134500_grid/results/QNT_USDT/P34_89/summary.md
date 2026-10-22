# EMA Hourly Continuation — QNT/USDT P34_89

**Symbol:** QNT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 831 |
| net_profit_factor | 0.4491 |
| net_win_rate | 0.4452 |
| gross_profit_factor | 0.8243 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -6.8159 |
| sortino_ratio | -2.7709 |
| max_drawdown | 0.9679 |
| cagr | -0.7420 |
| net_avg_win | 21.2950 |
| net_avg_loss | -38.0609 |
| avg_hold_time_bars | 5.7341 |
| exposure | 0.2166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
