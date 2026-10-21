# EMA Hourly Continuation — DEXE/USDT P20_89

**Symbol:** DEXE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.8468 |
| net_win_rate | 0.5188 |
| gross_profit_factor | 1.0550 |
| gross_win_rate | 0.5188 |
| sharpe_ratio | -0.9386 |
| sortino_ratio | -0.2785 |
| max_drawdown | 0.3843 |
| cagr | -0.1226 |
| net_avg_win | 70.0589 |
| net_avg_loss | -89.1864 |
| avg_hold_time_bars | 26.4906 |
| exposure | 0.5130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
