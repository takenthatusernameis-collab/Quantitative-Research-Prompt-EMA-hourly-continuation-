# EMA Hourly Continuation — ETH/USDT P55_200

**Symbol:** ETH/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.6770 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9335 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -1.8194 |
| sortino_ratio | -0.4158 |
| max_drawdown | 0.4036 |
| cagr | -0.1732 |
| net_avg_win | 63.6919 |
| net_avg_loss | -90.4600 |
| avg_hold_time_bars | 31.5725 |
| exposure | 0.3660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
