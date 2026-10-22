# EMA Hourly Continuation — SUI/USDT P50_89

**Symbol:** SUI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.5483 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9641 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -5.4413 |
| sortino_ratio | -2.0199 |
| max_drawdown | 0.9167 |
| cagr | -0.6224 |
| net_avg_win | 34.3227 |
| net_avg_loss | -55.7023 |
| avg_hold_time_bars | 4.0875 |
| exposure | 0.1275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
