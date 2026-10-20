# EMA Hourly Continuation — CHR/USDT P8_34

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1362 |
| net_profit_factor | 0.5090 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.8687 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -8.2806 |
| sortino_ratio | -4.2824 |
| max_drawdown | 0.9948 |
| cagr | -0.8749 |
| net_avg_win | 17.4207 |
| net_avg_loss | -26.3121 |
| avg_hold_time_bars | 5.5969 |
| exposure | 0.3449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
