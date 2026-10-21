# EMA Hourly Continuation — FLUX/USDT P8_200

**Symbol:** FLUX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 1.2228 |
| net_win_rate | 0.5830 |
| gross_profit_factor | 1.4107 |
| gross_win_rate | 0.5830 |
| sharpe_ratio | 1.0219 |
| sortino_ratio | 0.2476 |
| max_drawdown | 0.0956 |
| cagr | 0.1055 |
| net_avg_win | 99.5366 |
| net_avg_loss | -113.8146 |
| avg_hold_time_bars | 67.1144 |
| exposure | 0.8267 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
