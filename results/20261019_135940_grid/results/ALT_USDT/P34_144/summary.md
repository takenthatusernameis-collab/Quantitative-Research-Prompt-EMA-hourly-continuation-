# EMA Hourly Continuation — ALT/USDT P34_144

**Symbol:** ALT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6800 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9062 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -2.5291 |
| sortino_ratio | -0.7743 |
| max_drawdown | 0.6029 |
| cagr | -0.3029 |
| net_avg_win | 56.7941 |
| net_avg_loss | -76.6425 |
| avg_hold_time_bars | 20.3004 |
| exposure | 0.4300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
