# EMA Hourly Continuation — RUNE/USDT P12_21

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1469 |
| net_profit_factor | 0.2874 |
| net_win_rate | 0.3880 |
| gross_profit_factor | 0.7228 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -14.4059 |
| sortino_ratio | -7.9035 |
| max_drawdown | 1.0000 |
| cagr | -0.9846 |
| net_avg_win | 7.0767 |
| net_avg_loss | -15.6100 |
| avg_hold_time_bars | 2.1831 |
| exposure | 0.1458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
