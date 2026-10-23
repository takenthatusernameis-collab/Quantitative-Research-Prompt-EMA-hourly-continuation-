# EMA Hourly Continuation — ILV/USDT P12_50

**Symbol:** ILV/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.5807 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.9482 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -6.1680 |
| sortino_ratio | -2.8496 |
| max_drawdown | 0.9681 |
| cagr | -0.7455 |
| net_avg_win | 26.5976 |
| net_avg_loss | -40.4975 |
| avg_hold_time_bars | 6.8147 |
| exposure | 0.3327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
