# EMA Hourly Continuation — ICP/USDT P12_20

**Symbol:** ICP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1538 |
| net_profit_factor | 0.2750 |
| net_win_rate | 0.3843 |
| gross_profit_factor | 0.7074 |
| gross_win_rate | 0.4194 |
| sharpe_ratio | -14.8935 |
| sortino_ratio | -8.4024 |
| max_drawdown | 1.0000 |
| cagr | -0.9877 |
| net_avg_win | 6.4188 |
| net_avg_loss | -14.5653 |
| avg_hold_time_bars | 1.8095 |
| exposure | 0.1265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
