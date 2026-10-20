# EMA Hourly Continuation — 1INCH/USDT P12_34

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1326 |
| net_profit_factor | 0.4217 |
| net_win_rate | 0.4314 |
| gross_profit_factor | 0.8348 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -10.1098 |
| sortino_ratio | -5.1870 |
| max_drawdown | 0.9986 |
| cagr | -0.9254 |
| net_avg_win | 12.7291 |
| net_avg_loss | -22.8995 |
| avg_hold_time_bars | 4.3824 |
| exposure | 0.2641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
