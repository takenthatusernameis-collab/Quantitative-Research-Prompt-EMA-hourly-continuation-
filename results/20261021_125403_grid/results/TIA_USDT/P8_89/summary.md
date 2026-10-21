# EMA Hourly Continuation — TIA/USDT P8_89

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.9207 |
| net_win_rate | 0.5177 |
| gross_profit_factor | 1.0680 |
| gross_win_rate | 0.5177 |
| sharpe_ratio | -0.5249 |
| sortino_ratio | -0.1653 |
| max_drawdown | 0.3110 |
| cagr | -0.0787 |
| net_avg_win | 86.9966 |
| net_avg_loss | -101.4489 |
| avg_hold_time_bars | 30.0418 |
| exposure | 0.6541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
