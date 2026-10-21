# EMA Hourly Continuation — BLUR/USDT P12_20

**Symbol:** BLUR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.5696 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.8163 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -3.7055 |
| sortino_ratio | -1.0605 |
| max_drawdown | 0.7110 |
| cagr | -0.3857 |
| net_avg_win | 52.3018 |
| net_avg_loss | -73.3763 |
| avg_hold_time_bars | 4.3077 |
| exposure | 0.0786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
