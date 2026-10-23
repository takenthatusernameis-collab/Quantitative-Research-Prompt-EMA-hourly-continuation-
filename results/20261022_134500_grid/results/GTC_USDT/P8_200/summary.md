# EMA Hourly Continuation — GTC/USDT P8_200

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.6673 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9306 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -2.4852 |
| sortino_ratio | -0.7215 |
| max_drawdown | 0.5945 |
| cagr | -0.2889 |
| net_avg_win | 56.5568 |
| net_avg_loss | -77.5300 |
| avg_hold_time_bars | 39.4075 |
| exposure | 0.7649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
