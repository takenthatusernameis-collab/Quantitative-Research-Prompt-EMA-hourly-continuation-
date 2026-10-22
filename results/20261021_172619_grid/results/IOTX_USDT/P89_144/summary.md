# EMA Hourly Continuation — IOTX/USDT P89_144

**Symbol:** IOTX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.8200 |
| net_win_rate | 0.5281 |
| gross_profit_factor | 1.1164 |
| gross_win_rate | 0.5281 |
| sharpe_ratio | -1.0751 |
| sortino_ratio | -0.2699 |
| max_drawdown | 0.3092 |
| cagr | -0.1173 |
| net_avg_win | 76.6011 |
| net_avg_loss | -104.5236 |
| avg_hold_time_bars | 7.3828 |
| exposure | 0.1017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
