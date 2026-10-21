# EMA Hourly Continuation — PYTH/USDT P50_55

**Symbol:** PYTH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 97 |
| net_profit_factor | 0.7934 |
| net_win_rate | 0.5155 |
| gross_profit_factor | 1.0571 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -0.6948 |
| sortino_ratio | -0.0986 |
| max_drawdown | 0.1497 |
| cagr | -0.0443 |
| net_avg_win | 82.6547 |
| net_avg_loss | -110.8321 |
| avg_hold_time_bars | 3.4227 |
| exposure | 0.0151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
