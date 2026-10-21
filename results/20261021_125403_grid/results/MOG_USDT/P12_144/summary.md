# EMA Hourly Continuation — MOG/USDT P12_144

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8684 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9861 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -0.8438 |
| sortino_ratio | -0.2312 |
| max_drawdown | 0.3268 |
| cagr | -0.1038 |
| net_avg_win | 87.9525 |
| net_avg_loss | -100.0809 |
| avg_hold_time_bars | 40.0387 |
| exposure | 0.6688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
