# EMA Hourly Continuation — IMX/USDT P12_144

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.8501 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 0.9943 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -0.8694 |
| sortino_ratio | -0.2408 |
| max_drawdown | 0.2764 |
| cagr | -0.1076 |
| net_avg_win | 74.9104 |
| net_avg_loss | -89.0589 |
| avg_hold_time_bars | 39.5452 |
| exposure | 0.6728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
