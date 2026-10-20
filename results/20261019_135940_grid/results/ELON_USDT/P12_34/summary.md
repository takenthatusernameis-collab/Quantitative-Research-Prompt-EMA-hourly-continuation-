# EMA Hourly Continuation — ELON/USDT P12_34

**Symbol:** ELON/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1213 |
| net_profit_factor | 0.3833 |
| net_win_rate | 0.4188 |
| gross_profit_factor | 0.7243 |
| gross_win_rate | 0.4246 |
| sharpe_ratio | -9.8738 |
| sortino_ratio | -4.9057 |
| max_drawdown | 0.9974 |
| cagr | -0.9067 |
| net_avg_win | 12.2008 |
| net_avg_loss | -22.9392 |
| avg_hold_time_bars | 4.6216 |
| exposure | 0.2548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
