# EMA Hourly Continuation — SKY/USDT P8_34

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1105 |
| net_profit_factor | 0.4832 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -8.5727 |
| sortino_ratio | -4.4301 |
| max_drawdown | 0.9888 |
| cagr | -0.8878 |
| net_avg_win | 18.5594 |
| net_avg_loss | -31.5139 |
| avg_hold_time_bars | 5.4787 |
| exposure | 0.3376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
