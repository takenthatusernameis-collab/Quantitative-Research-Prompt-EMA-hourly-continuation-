# EMA Hourly Continuation — ERG/USDT P20_21

**Symbol:** ERG/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 143 |
| net_profit_factor | 0.4093 |
| net_win_rate | 0.3636 |
| gross_profit_factor | 0.6112 |
| gross_win_rate | 0.3636 |
| sharpe_ratio | -3.4402 |
| sortino_ratio | -0.5813 |
| max_drawdown | 0.5054 |
| cagr | -0.2419 |
| net_avg_win | 66.7963 |
| net_avg_loss | -93.2466 |
| avg_hold_time_bars | 4.6503 |
| exposure | 0.0302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
