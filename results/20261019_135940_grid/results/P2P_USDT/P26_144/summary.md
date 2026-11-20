# EMA Hourly Continuation — P2P/USDT P26_144

**Symbol:** P2P/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.5855 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.7674 |
| gross_win_rate | 0.4294 |
| sharpe_ratio | -3.6836 |
| sortino_ratio | -1.1394 |
| max_drawdown | 0.7539 |
| cagr | -0.4191 |
| net_avg_win | 50.3141 |
| net_avg_loss | -64.1427 |
| avg_hold_time_bars | 19.7035 |
| exposure | 0.4380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
