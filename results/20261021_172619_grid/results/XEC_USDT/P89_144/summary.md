# EMA Hourly Continuation — XEC/USDT P89_144

**Symbol:** XEC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.5753 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8425 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -3.1923 |
| sortino_ratio | -0.8195 |
| max_drawdown | 0.6210 |
| cagr | -0.3144 |
| net_avg_win | 56.6046 |
| net_avg_loss | -81.7080 |
| avg_hold_time_bars | 7.8457 |
| exposure | 0.1150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
