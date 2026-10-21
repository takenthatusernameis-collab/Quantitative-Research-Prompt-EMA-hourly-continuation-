# EMA Hourly Continuation — AMP/USDT P12_26

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.4312 |
| net_win_rate | 0.3942 |
| gross_profit_factor | 0.6342 |
| gross_win_rate | 0.3942 |
| sharpe_ratio | -5.7605 |
| sortino_ratio | -1.8722 |
| max_drawdown | 0.8875 |
| cagr | -0.5794 |
| net_avg_win | 32.7785 |
| net_avg_loss | -49.4713 |
| avg_hold_time_bars | 5.2212 |
| exposure | 0.1234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
