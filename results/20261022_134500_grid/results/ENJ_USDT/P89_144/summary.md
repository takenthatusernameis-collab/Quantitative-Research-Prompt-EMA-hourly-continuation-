# EMA Hourly Continuation — ENJ/USDT P89_144

**Symbol:** ENJ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.5493 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.9652 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -4.4911 |
| sortino_ratio | -1.3976 |
| max_drawdown | 0.8193 |
| cagr | -0.4880 |
| net_avg_win | 44.5488 |
| net_avg_loss | -69.0325 |
| avg_hold_time_bars | 5.3505 |
| exposure | 0.1174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
