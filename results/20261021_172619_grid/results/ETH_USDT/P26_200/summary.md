# EMA Hourly Continuation — ETH/USDT P26_200

**Symbol:** ETH/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.7075 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9600 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.4860 |
| sortino_ratio | -0.3080 |
| max_drawdown | 0.3304 |
| cagr | -0.1318 |
| net_avg_win | 69.4786 |
| net_avg_loss | -96.3524 |
| avg_hold_time_bars | 67.3714 |
| exposure | 0.6431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
