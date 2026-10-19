# EMA Hourly Continuation — TRX/USDT P8_34

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1203 |
| net_profit_factor | 0.2128 |
| net_win_rate | 0.3608 |
| gross_profit_factor | 0.8970 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -15.0965 |
| sortino_ratio | -7.6885 |
| max_drawdown | 1.0000 |
| cagr | -0.9854 |
| net_avg_win | 6.2278 |
| net_avg_loss | -16.5183 |
| avg_hold_time_bars | 5.9618 |
| exposure | 0.3260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
