# EMA Hourly Continuation — POL/USDT P20_144

**Symbol:** POL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.9890 |
| net_win_rate | 0.5489 |
| gross_profit_factor | 1.2119 |
| gross_win_rate | 0.5489 |
| sharpe_ratio | -0.0018 |
| sortino_ratio | -0.0005 |
| max_drawdown | 0.2529 |
| cagr | -0.0065 |
| net_avg_win | 83.4522 |
| net_avg_loss | -102.6740 |
| avg_hold_time_bars | 42.6057 |
| exposure | 0.6139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
