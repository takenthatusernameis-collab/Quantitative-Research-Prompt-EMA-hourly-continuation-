# EMA Hourly Continuation — ID/USDT P34_144

**Symbol:** ID/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7511 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9441 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.6713 |
| sortino_ratio | -0.4764 |
| max_drawdown | 0.4321 |
| cagr | -0.1973 |
| net_avg_win | 65.5326 |
| net_avg_loss | -83.8243 |
| avg_hold_time_bars | 20.9275 |
| exposure | 0.3788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
