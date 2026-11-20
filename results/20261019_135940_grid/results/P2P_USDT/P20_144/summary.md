# EMA Hourly Continuation — P2P/USDT P20_144

**Symbol:** P2P/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.5457 |
| net_win_rate | 0.4157 |
| gross_profit_factor | 0.7026 |
| gross_win_rate | 0.4176 |
| sharpe_ratio | -4.0111 |
| sortino_ratio | -1.2694 |
| max_drawdown | 0.7910 |
| cagr | -0.4526 |
| net_avg_win | 44.1856 |
| net_avg_loss | -57.6027 |
| avg_hold_time_bars | 21.3980 |
| exposure | 0.4960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
