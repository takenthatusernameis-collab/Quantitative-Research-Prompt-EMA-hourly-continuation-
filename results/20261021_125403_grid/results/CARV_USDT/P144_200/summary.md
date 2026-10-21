# EMA Hourly Continuation — CARV/USDT P144_200

**Symbol:** CARV/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 182 |
| net_profit_factor | 0.7177 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0076 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -1.4877 |
| sortino_ratio | -0.3204 |
| max_drawdown | 0.2831 |
| cagr | -0.1372 |
| net_avg_win | 71.4590 |
| net_avg_loss | -101.7846 |
| avg_hold_time_bars | 8.6374 |
| exposure | 0.0885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
