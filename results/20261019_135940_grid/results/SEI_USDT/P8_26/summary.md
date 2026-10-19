# EMA Hourly Continuation — SEI/USDT P8_26

**Symbol:** SEI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1548 |
| net_profit_factor | 0.5162 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8744 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -9.5928 |
| sortino_ratio | -5.3340 |
| max_drawdown | 0.9986 |
| cagr | -0.9262 |
| net_avg_win | 15.4395 |
| net_avg_loss | -24.0547 |
| avg_hold_time_bars | 3.9367 |
| exposure | 0.2770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
