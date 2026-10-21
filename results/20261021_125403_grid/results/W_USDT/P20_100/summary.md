# EMA Hourly Continuation — W/USDT P20_100

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.8624 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 1.0304 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -1.0578 |
| sortino_ratio | -0.3318 |
| max_drawdown | 0.4057 |
| cagr | -0.1445 |
| net_avg_win | 83.6285 |
| net_avg_loss | -99.8479 |
| avg_hold_time_bars | 18.6660 |
| exposure | 0.4064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
