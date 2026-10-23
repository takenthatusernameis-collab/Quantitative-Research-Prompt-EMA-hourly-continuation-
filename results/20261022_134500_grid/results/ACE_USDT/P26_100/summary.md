# EMA Hourly Continuation — ACE/USDT P26_100

**Symbol:** ACE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.7310 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0570 |
| gross_win_rate | 0.5186 |
| sharpe_ratio | -2.1259 |
| sortino_ratio | -0.6977 |
| max_drawdown | 0.5750 |
| cagr | -0.2786 |
| net_avg_win | 55.6528 |
| net_avg_loss | -79.0207 |
| avg_hold_time_bars | 14.0743 |
| exposure | 0.3427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
