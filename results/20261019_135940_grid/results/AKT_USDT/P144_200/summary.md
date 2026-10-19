# EMA Hourly Continuation — AKT/USDT P144_200

**Symbol:** AKT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.4902 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.9265 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -3.9530 |
| sortino_ratio | -1.0686 |
| max_drawdown | 0.7533 |
| cagr | -0.4173 |
| net_avg_win | 39.8800 |
| net_avg_loss | -73.1779 |
| avg_hold_time_bars | 4.3016 |
| exposure | 0.0739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
