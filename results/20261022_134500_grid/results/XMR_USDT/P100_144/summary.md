# EMA Hourly Continuation — XMR/USDT P100_144

**Symbol:** XMR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.2526 |
| net_win_rate | 0.3852 |
| gross_profit_factor | 0.6748 |
| gross_win_rate | 0.4053 |
| sharpe_ratio | -10.1784 |
| sortino_ratio | -4.1259 |
| max_drawdown | 0.9953 |
| cagr | -0.8811 |
| net_avg_win | 10.9552 |
| net_avg_loss | -27.1748 |
| avg_hold_time_bars | 2.7139 |
| exposure | 0.0983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
