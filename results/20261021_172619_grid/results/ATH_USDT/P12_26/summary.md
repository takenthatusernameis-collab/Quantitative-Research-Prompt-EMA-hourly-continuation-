# EMA Hourly Continuation — ATH/USDT P12_26

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.7622 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0050 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.6857 |
| sortino_ratio | -0.4812 |
| max_drawdown | 0.4142 |
| cagr | -0.1980 |
| net_avg_win | 69.8390 |
| net_avg_loss | -92.1206 |
| avg_hold_time_bars | 5.5067 |
| exposure | 0.0990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
