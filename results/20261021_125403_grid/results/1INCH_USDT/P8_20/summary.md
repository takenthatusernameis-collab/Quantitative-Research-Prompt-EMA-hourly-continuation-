# EMA Hourly Continuation — 1INCH/USDT P8_20

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.6013 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.8908 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -3.8200 |
| sortino_ratio | -1.3181 |
| max_drawdown | 0.7846 |
| cagr | -0.4529 |
| net_avg_win | 42.6323 |
| net_avg_loss | -64.7925 |
| avg_hold_time_bars | 5.3183 |
| exposure | 0.1397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
