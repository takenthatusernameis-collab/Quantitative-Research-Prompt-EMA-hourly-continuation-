# EMA Hourly Continuation — AMP/USDT P8_200

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.4242 |
| net_win_rate | 0.4037 |
| gross_profit_factor | 0.6948 |
| gross_win_rate | 0.4171 |
| sharpe_ratio | -6.7006 |
| sortino_ratio | -2.5753 |
| max_drawdown | 0.9571 |
| cagr | -0.7107 |
| net_avg_win | 23.3136 |
| net_avg_loss | -37.2125 |
| avg_hold_time_bars | 21.4706 |
| exposure | 0.7300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
