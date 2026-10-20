# EMA Hourly Continuation — CHR/USDT P12_26

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1354 |
| net_profit_factor | 0.4207 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.8656 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -9.4271 |
| sortino_ratio | -4.9090 |
| max_drawdown | 0.9975 |
| cagr | -0.9070 |
| net_avg_win | 12.3817 |
| net_avg_loss | -22.3905 |
| avg_hold_time_bars | 3.4705 |
| exposure | 0.2126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
