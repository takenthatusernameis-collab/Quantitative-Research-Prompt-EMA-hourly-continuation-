# EMA Hourly Continuation — ID/USDT P26_144

**Symbol:** ID/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.8254 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0164 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -1.1040 |
| sortino_ratio | -0.3175 |
| max_drawdown | 0.3195 |
| cagr | -0.1376 |
| net_avg_win | 71.8546 |
| net_avg_loss | -89.6819 |
| avg_hold_time_bars | 27.6510 |
| exposure | 0.5055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
