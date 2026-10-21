# EMA Hourly Continuation — JTO/USDT P34_144

**Symbol:** JTO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7772 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -1.4861 |
| sortino_ratio | -0.4083 |
| max_drawdown | 0.4158 |
| cagr | -0.1719 |
| net_avg_win | 73.9416 |
| net_avg_loss | -87.2882 |
| avg_hold_time_bars | 21.5323 |
| exposure | 0.3641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
