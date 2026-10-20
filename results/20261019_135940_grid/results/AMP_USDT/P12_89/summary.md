# EMA Hourly Continuation — AMP/USDT P12_89

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1102 |
| net_profit_factor | 0.3944 |
| net_win_rate | 0.3848 |
| gross_profit_factor | 0.6706 |
| gross_win_rate | 0.3984 |
| sharpe_ratio | -9.7852 |
| sortino_ratio | -4.5648 |
| max_drawdown | 0.9965 |
| cagr | -0.8939 |
| net_avg_win | 15.3044 |
| net_avg_loss | -24.2674 |
| avg_hold_time_bars | 10.1515 |
| exposure | 0.5085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
