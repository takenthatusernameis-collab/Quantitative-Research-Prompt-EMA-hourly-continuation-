# EMA Hourly Continuation — ARB/USDT P20_34

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.6718 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9317 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -1.9846 |
| sortino_ratio | -0.4760 |
| max_drawdown | 0.4514 |
| cagr | -0.1946 |
| net_avg_win | 63.1157 |
| net_avg_loss | -88.7306 |
| avg_hold_time_bars | 5.8857 |
| exposure | 0.0749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
