# EMA Hourly Continuation — AMP/USDT P12_55

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1416 |
| net_profit_factor | 0.3651 |
| net_win_rate | 0.3863 |
| gross_profit_factor | 0.6929 |
| gross_win_rate | 0.4040 |
| sharpe_ratio | -11.9034 |
| sortino_ratio | -6.3024 |
| max_drawdown | 0.9996 |
| cagr | -0.9574 |
| net_avg_win | 10.5111 |
| net_avg_loss | -18.1196 |
| avg_hold_time_bars | 6.0530 |
| exposure | 0.3896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
