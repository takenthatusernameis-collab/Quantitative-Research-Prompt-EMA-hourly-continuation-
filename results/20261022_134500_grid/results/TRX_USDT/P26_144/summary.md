# EMA Hourly Continuation — TRX/USDT P26_144

**Symbol:** TRX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.3054 |
| net_win_rate | 0.3972 |
| gross_profit_factor | 0.8741 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -7.8738 |
| sortino_ratio | -2.4811 |
| max_drawdown | 0.9683 |
| cagr | -0.7431 |
| net_avg_win | 21.3689 |
| net_avg_loss | -46.1023 |
| avg_hold_time_bars | 18.0619 |
| exposure | 0.4113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
