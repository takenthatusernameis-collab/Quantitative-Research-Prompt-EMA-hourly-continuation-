# EMA Hourly Continuation — RENDER/USDT P8_200

**Symbol:** RENDER/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.9713 |
| net_win_rate | 0.5255 |
| gross_profit_factor | 1.0876 |
| gross_win_rate | 0.5255 |
| sharpe_ratio | -0.0855 |
| sortino_ratio | -0.0185 |
| max_drawdown | 0.1955 |
| cagr | -0.0126 |
| net_avg_win | 88.7443 |
| net_avg_loss | -101.1918 |
| avg_hold_time_bars | 82.3316 |
| exposure | 0.8517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
