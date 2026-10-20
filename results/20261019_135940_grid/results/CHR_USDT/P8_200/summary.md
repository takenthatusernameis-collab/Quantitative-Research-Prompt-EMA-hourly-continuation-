# EMA Hourly Continuation — CHR/USDT P8_200

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.6826 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.8935 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -2.1590 |
| sortino_ratio | -0.5631 |
| max_drawdown | 0.5462 |
| cagr | -0.2349 |
| net_avg_win | 64.7858 |
| net_avg_loss | -84.9991 |
| avg_hold_time_bars | 52.6812 |
| exposure | 0.8224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
