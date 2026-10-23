# EMA Hourly Continuation — AMP/USDT P8_100

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1093 |
| net_profit_factor | 0.3586 |
| net_win_rate | 0.3843 |
| gross_profit_factor | 0.6086 |
| gross_win_rate | 0.4035 |
| sharpe_ratio | -9.4534 |
| sortino_ratio | -4.4039 |
| max_drawdown | 0.9955 |
| cagr | -0.8819 |
| net_avg_win | 13.2485 |
| net_avg_loss | -23.0573 |
| avg_hold_time_bars | 12.1080 |
| exposure | 0.6015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
