# EMA Hourly Continuation — GRT/USDT P12_144

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.9009 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0809 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -0.5877 |
| sortino_ratio | -0.1546 |
| max_drawdown | 0.3196 |
| cagr | -0.0721 |
| net_avg_win | 88.9142 |
| net_avg_loss | -107.8886 |
| avg_hold_time_bars | 44.5727 |
| exposure | 0.6797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
