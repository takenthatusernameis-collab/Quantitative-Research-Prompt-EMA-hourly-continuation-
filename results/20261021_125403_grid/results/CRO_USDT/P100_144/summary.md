# EMA Hourly Continuation — CRO/USDT P100_144

**Symbol:** CRO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.5744 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8944 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -2.6295 |
| sortino_ratio | -0.5699 |
| max_drawdown | 0.4913 |
| cagr | -0.2293 |
| net_avg_win | 60.5584 |
| net_avg_loss | -93.2331 |
| avg_hold_time_bars | 6.8640 |
| exposure | 0.0711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
