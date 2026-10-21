# EMA Hourly Continuation — XNO/USDT P20_55

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.6522 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.8649 |
| gross_win_rate | 0.4566 |
| sharpe_ratio | -3.3236 |
| sortino_ratio | -1.0898 |
| max_drawdown | 0.7443 |
| cagr | -0.3935 |
| net_avg_win | 55.4028 |
| net_avg_loss | -71.3840 |
| avg_hold_time_bars | 7.4094 |
| exposure | 0.1785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
