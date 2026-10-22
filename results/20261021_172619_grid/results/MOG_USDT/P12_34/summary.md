# EMA Hourly Continuation — MOG/USDT P12_34

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.7694 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.9315 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -2.5205 |
| sortino_ratio | -0.8749 |
| max_drawdown | 0.6384 |
| cagr | -0.3319 |
| net_avg_win | 78.6925 |
| net_avg_loss | -90.9167 |
| avg_hold_time_bars | 7.7574 |
| exposure | 0.2098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
